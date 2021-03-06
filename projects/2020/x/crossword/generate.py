from operator import ne
import sys

from crossword import *
from collections import deque


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for var, vals in self.domains.items():
            for val in vals.copy():
                if len(val) != var.length:
                    self.domains[var].remove(val)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        overlap = self.crossword.overlaps[x, y]
        if not overlap:
            return False

        revised = False
        for x_val in self.domains[x].copy():
            consistent = False
            for y_val in self.domains[y].copy():
                if x_val[overlap[0]] == y_val[overlap[1]]:
                    consistent = True
                    break
            if not consistent:
                self.domains[x].remove(x_val)
                revised = True

        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        queue = deque()
        if not arcs:
            for x in self.crossword.variables:
                for y in self.crossword.variables:
                    if x != y and self.crossword.overlaps[x, y]:
                        queue.append((x, y))
        else:
            queue = deque(arcs)

        while len(queue) != 0:
            x, y = queue.popleft()
            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False
                for neighbor in self.crossword.neighbors(x):
                    if neighbor != y:
                        queue.append((neighbor, x))

        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        return len(assignment) == len(self.crossword.variables)

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        exists = []
        for var, val in assignment.items():
            if var.length != len(val) or val in exists:
                return False
            for neighbor in self.crossword.neighbors(var):
                if neighbor not in assignment.keys():
                    continue
                overlap = self.crossword.overlaps[var, neighbor]
                if val[overlap[0]] != assignment[neighbor][overlap[1]]:
                    return False
            exists.append(val)

        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        values = []
        for val in self.domains[var]:
            cnt = 0
            for neighbor in self.crossword.neighbors(var):
                if not(neighbor in assignment or val not in self.domains[neighbor]):
                    cnt += 1
            values.append((val, cnt))

        values.sort(key=lambda value: value[1])
        
        result = []
        for value in values:
            result.append(value[0])

        return result

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        mrv_domains = []
        for var, val in self.domains.items():
            if var not in assignment:    
                mrv_domains.append((var, len(val)))
        mrv_domains.sort(key=lambda domain: domain[1])

        degree_domains = []
        for var, size in mrv_domains:
            if size > mrv_domains[0][1]:
                break
            degree_domains.append((var, len(self.crossword.neighbors(var))))

        return sorted(degree_domains, key=lambda domain: domain[1])[0][0]

    def inferences(self, var, assignment):
        self.domains[var].clear()
        self.domains[var].add(assignment[var])

        arcs = []
        for neighbor in self.crossword.neighbors(var):
            if neighbor not in assignment:
                arcs.append((neighbor, var))

        if not self.ac3(arcs):
            return None
        
        results = []
        for var, val in self.domains.items():
            if var not in assignment and len(val) == 1:
                results.append((var, next(iter(val))))    

        return results

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """        
        if self.assignment_complete(assignment):
            return assignment

        var = self.select_unassigned_variable(assignment)
        for val in self.order_domain_values(var, assignment):
            assignment[var] = val
            domains = self.domains.copy()
            inferences = self.inferences(var, assignment)
            if self.consistent(assignment):
                if inferences:
                    for inference in inferences:
                        assignment[inference[0]] = inference[1]
                result = self.backtrack(assignment)
                if result:
                    return result
            del assignment[var]
            if inferences:
                for inference in inferences:
                    del assignment[inference[0]]
            self.domains = domains
        
        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
