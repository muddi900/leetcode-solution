function canConstructCounter(s: string, k: number): boolean {
  if (s.length < k) {
    return false;
  }

  if (s.length === k) {
    return true;
  }
  const c = new Map<string, number>();

  for (const char of s) {
    c.set(char, (c.get(char) || 0) + 1);
  }

  let count = 0;

  for (const [_, v] of c) {
    if (v % 2 === 0) {
      count++;
    }
  }

  return count <= k;
}

function canConstructMemo(s: string, k: number): boolean {
  if (s.length < k) {
    return false;
  }

  if (s.length === k) {
    return true;
  }

  const c = new Array(26);

  for (const char of s) {
    c[char.codePointAt(0)! - "a".codePointAt(0)!] =
      (char.codePointAt(0)! || 0) + 1;
  }

  let count = 0;
  for (const v of c) {
    if (v % 2 === 0) {
      count++;
    }
  }

  return count <= k;
}

const s1 = "annabelle", k1 = 2;
const s2 = "leetcode", k2 = 3;
const s3 = "true", k3 = 4;

Deno.bench("Counter", () => {
  canConstructCounter(s1, k1);
  canConstructCounter(s2, k2);
  canConstructCounter(s3, k3);
});

Deno.bench("Memo", () => {
  canConstructMemo(s1, k1);
  canConstructMemo(s2, k2);
  canConstructMemo(s3, k3);
});

// Learn more at https://docs.deno.com/runtime/manual/examples/module_metadata#concepts
