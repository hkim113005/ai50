from dis import dis
from importlib.metadata import distribution
import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    distribution = {}

    for state in corpus:
        distribution[state] = 0
    for state, links in corpus.items():
        distribution[state] += ((1 - damping_factor) / len(corpus))
        if state == page:
            for link in links:
                distribution[link] += (damping_factor / len(links))
            if len(links) == 0:
                for state in distribution:
                    distribution[state] += (damping_factor / len(corpus))

    return distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    ranks = {}
    for state in corpus:
        ranks[state] = 0
    page = random.choices(list(corpus.keys()))[0]
    ranks[page] += 1
    
    for i in range(n):
        distribution = transition_model(corpus, page, damping_factor)
        page = random.choices(list(distribution.keys()), list(distribution.values()))[0]
        ranks[page] += 1

    for state in ranks:
        ranks[state] /= n

    return ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    ranks = {}
    for state in corpus:
        ranks[state] = 1 / len(corpus)

    while (True):
        new_ranks = {}
        for state in corpus:
            new_ranks[state] = (1 - damping_factor) / len(corpus)
            for i, links in corpus.items():
                if state in links:
                    new_ranks[state] += damping_factor * (ranks[i] / len(corpus[i]))
        
        stop = True
        for state in corpus:
            if abs(ranks[state] - new_ranks[state]) >= 0.001:
                stop = False

        ranks = new_ranks

        if stop:
            break

    return ranks


if __name__ == "__main__":
    main()
