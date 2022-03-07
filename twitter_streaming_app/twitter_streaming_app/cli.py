"""Console script for twitter_streaming_app."""
import argparse
import sys
import twitter_streaming_app
from twitter_streaming_app.twitter_auth import twitter_auth



def main():
    """Console script for twitter_streaming_app."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()
    app = twitter_auth().auth()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "twitter_streaming_app.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
