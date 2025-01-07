export function stringMatching(words: string[]): string[] {
  const sorted = words.toSorted((a, b) => b.length - a.length);
  const answer: Set<string> = new Set();

  for (let i = 0; i < sorted.length; i++) {
    for (let j = i + 1; j < sorted.length; j++) {
      if (sorted[i].indexOf(sorted[j]) > -1) {
        answer.add(sorted[j]);
      }
    }
  }

  return Array.from(answer);
}

// Learn more at https://docs.deno.com/runtime/manual/examples/module_metadata#concepts
if (import.meta.main) {
  console.log(stringMatching(["mass", "as", "hero", "superhero"]));
  console.log(stringMatching(["leetcode", "et", "code"]));
  console.log(stringMatching(["blue", "green", "bu"]));
}
