#!/usr/bin/env python3
import brain_games.cli


def start_text():
    print("Welcome to the Brain Games!")


def main():
    start_text()
    brain_games.cli.welcome_user()


if __name__ == '__main__':
    main()
