package main

import "fmt"

func isPrefixAndSuffix(ss string, s string) bool {
	ssLength := len(ss)
	sLength := len(s)

	if ssLength >= sLength {
		return false
	}

	return s[:ssLength] == ss && s[sLength-ssLength:] == ss

}

func countPrefixSuffixPairs(words []string) int {

	count := 0

	for i, word := range words {
		for j := i + 1; j < len(words); j++ {
			sub := words[j]

			if isPrefixAndSuffix(word, sub) {
				count++
			}
		}
	}

	return count
}

func main() {
	fmt.Println(countPrefixSuffixPairs([]string{"a", "aba", "ababa", "aa"}))
	fmt.Println(countPrefixSuffixPairs([]string{"pa", "papa", "ma", "mama"}))
	fmt.Println(countPrefixSuffixPairs([]string{"ababa", "ab"}))
}
