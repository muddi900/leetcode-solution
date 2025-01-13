package main

import "fmt"

func minimumLength(s string) int {
	if len(s) <= 2 {
		return len(s)
	}

	counter := make([]int, 26)

	for _, r := range s {
		counter[r-'a'] += 1
	}

	min_size := len(s)

	for _, freq := range counter {
		if freq <= 2 {
			continue
		}
		if freq%2 == 0 {
			min_size -= freq - 2
			continue
		}

		min_size -= freq - 1

	}

	return min_size
}

func main() {
	fmt.Println(minimumLength("abaacbcbb"))
	fmt.Println(minimumLength("aa"))
}
