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
    if (v % 2 > 0) {
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
    const index = char.codePointAt(0)! - "a".codePointAt(0)!;
    c[index] = (c[index] || 0) + 1;
  }

  let count = 0;
  for (const v of c) {
    if (v % 2 > 0) {
      count++;
    }
  }

  return count <= k;
}

function canConstructMemoDirect(s: string, k: number): boolean {
  if (s.length < k) {
    return false;
  }

  if (s.length === k) {
    return true;
  }

  const c = new Array(26);

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    const index = char.codePointAt(0)! - "a".codePointAt(0)!;
    c[index] = (c[index] || 0) + 1;
  }

  let count = 0;
  for (let i = 0; i < c.length; i++) {
    const v = c[i];
    if (v % 2 > 0) {
      count++;
    }
  }

  return count <= k;
}

const s1 = "annabelle", k1 = 2;
const s2 = "leetcode", k2 = 3;
const s3 = "true", k3 = 4;

// console.log(canConstructMemo(s1, k1));
// console.log(canConstructCounter(s1, k1));
// console.log(canConstructMemo(s2, k2));
// console.log(canConstructCounter(s2, k2));

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

Deno.bench("MemoDirect", () => {
  canConstructMemoDirect(s1, k1);
  canConstructMemoDirect(s2, k2);
  canConstructMemoDirect(s3, k3);
});

// Learn more at https://docs.deno.com/runtime/manual/examples/module_metadata#concepts
