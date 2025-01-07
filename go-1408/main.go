package main

import (
	"fmt"
	"maps"
	"slices"
	"sort"
	"strings"
)

func stringMatching(words []string) []string {

	answer := map[string]bool{}

	sort.Slice(words, func(i, j int) bool {
		return len(words[i]) > len(words[j])
	})

	for i, word := range words {
		for j := i + 1; j < len(words); j++ {
			match_word := words[j]

			if strings.Contains(word, match_word) {
				answer[match_word] = true
			}
		}
	}

	return slices.Collect(maps.Keys(answer))

}

func main() {
	fmt.Println(stringMatching([]string{"mass", "as", "hero", "superhero"}))
	fmt.Println(stringMatching([]string{"leetcode", "et", "code"}))
	fmt.Println(stringMatching([]string{"blue", "green", "bu"}))

}
