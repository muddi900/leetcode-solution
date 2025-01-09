package main

import "fmt"

func main() {
	fmt.Println(prefixCount([]string{"pay", "attention", "practice", "attend"}, "at"))
	fmt.Println(prefixCount([]string{"pay", "attention", "practice", "attend"}, "code"))
}

func prefixCount(words []string, pref string) int {
	count := 0

	for _, word := range words {
		if len(pref) > len(word) {
			continue
		}
		if word[:len(pref)] == pref {
			count++
		}
	}

	return count
}
