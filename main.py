#!/usr/bin/env python3
import random

families = [
    ['Mike', 'Margie', 'MeMaw'],
    ['Kevin', 'Heather', 'Wesley', 'Ben', 'Zac'],
    ['Chris', 'Jamie', 'Kaylin', 'Brynlee'],
    ['Bill', 'Michelle', 'Will', 'Isaac'],
]

def main():
    all_members = [(member, family) for family in families for member in family]
    random.shuffle(all_members)

    givers = all_members.copy()
    receivers = all_members.copy()

    matches = []
    while givers:
        giver = givers.pop(0)
        valid_matches = [p for p in receivers if p[1] != giver[1]]

        if valid_matches:
            receiver = random.choice(valid_matches)
            receivers.remove(receiver)
            matches.append((giver[0], receiver[0]))
        else:
            print(f"Could not find match for {giver[0]}")

    unmatched = []

    while unmatched:
        person1 = unmatched.pop(0)
        valid_matches = [p for p in unmatched if p[1] != person1[1]]

        if valid_matches:
            person2 = random.choice(valid_matches)
            unmatched.remove(person2)
            matches.append((person1[0], person2[0]))
        else:
            print(f"Could not find match for {person1[0]}")

    print("Random Family Member Matches:")
    for match in matches:
        print(f"\t{match[0]} -> {match[1]}")


if __name__ == "__main__":
    main()

