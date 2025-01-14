package main

import "fmt"

func findThePrefixCommonArray(A []int, B []int) []int {
	n := len(A)

	count := 0
	ans := []int{}
	freq := make([]int, n+1)

	for i, a := range A {

		b := B[i]
		freq[a]++

		if freq[a] == 2 {
			count++
		}

		freq[b]++
		if freq[b] == 2 {
			count++
		}
		ans = append(ans, count)
	}

	return ans
}

func main() {
	fmt.Println(findThePrefixCommonArray(
		[]int{1, 3, 2, 4},
		[]int{3, 1, 2, 4},
	))

	fmt.Println(findThePrefixCommonArray(
		[]int{2, 3, 1},
		[]int{3, 1, 2},
	))

}
