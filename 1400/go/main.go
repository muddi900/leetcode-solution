package main

import "fmt"

func canConstruct(s string, k int) bool {
	if len(s) < k {
		return false
	}

	if len(s) == k {
		return true
	}
	c := make([]int, 26)
	count := 0

	for _, r := range s {
		c[r-'a']++
	}

	for _, v := range c {
		if v%2 > 0 {
			count++
		}
	}

	return count <= k
}

func main() {
	fmt.Println(canConstruct("annabelle", 2))
	fmt.Println(canConstruct("leetcode", 3))
	fmt.Println(canConstruct("true", 4))
}
