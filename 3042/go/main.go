package main

import "fmt"

type Node struct {
	children map[rune]*Node
	isEnd    bool
}

func NewNode() *Node {
	return &Node{children: make(map[rune]*Node)}
}

type Trie struct {
	root *Node
}

func initTrie() *Trie {
	return &Trie{root: NewNode()}
}

func (tr *Trie) Insert(word string) {
	node := tr.root

	for _, r := range word {
		if _, exists := node.children[r]; !exists {
			node.children[r] = NewNode()
		}

		node = node.children[r]
	}

	node.isEnd = true
}

func (tr *Trie) Search(word string) bool {
	node := tr.root

	for _, r := range word {
		if _, exists := node.children[r]; !exists {
			return false
		}

		node = node.children[r]
	}

	return true
}

func (tr *Trie) SearchReverse() {

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
