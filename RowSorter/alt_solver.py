def main():
    n_rows = int(input())
    rows = [input() for _ in range(n_rows)]

    longest = max(len(row) for row in rows)

    for row in rows:
        row = list(row.ljust(longest))
        row.sort(key=lambda x: {"+":0, " ":1, "*": 2}[x])
        print("".join(row))
        
if __name__ == "__main__":
    main()
