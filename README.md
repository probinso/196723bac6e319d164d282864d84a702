# Solution Description
Pure Python3 solution to Insight Coding Challenge, with updated `data-gen/get-tweets.py` for Python3 compliance.

Structures used to solve problem are described in `src/challenge/challibs.py`. `challibs.TimeGraph` is a structure that mantains a sliding window of time for edges of a graph. This will not produce useful results against edges with timestamps occuring before the *Unix Epock*.

`challibs.clean_tweets` provides a data ellis converting raw tweets in json into simple dictionaries with only critical information.

`src/challenge-runner.py` is the executable, python, CLI to the program.

## Repo directory structure

    .
    ├── data-gen
    │   ├── get-tweets.py
    │   ├── README.md
    │   └── tweets.txt
    ├── insight_testsuite
    │   ├── results.txt
    │   ├── run_tests.sh
    │   └── tests
    │       ├── one-tweet
    │       │   ├── ...
    │       └── test-2-tweets-all-distinct
    │           └── ...
    ├── README.md
    ├── run.sh
    ├── src
    │   ├── challenge
    │   │   ├── challibs.py
    │   │   └── tweetprocess.py
    │   └── challenge-runner.py
    ├── tweet_input
    │   └── tweets.txt -> ../data-gen/tweets.txt
    └── tweet_output
        └── output.txt


