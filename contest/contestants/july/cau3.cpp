#include <bits/stdc++.h>
using namespace std;

const int NMAX = 2e5;

struct Hash {
  int BASE, MOD;
  long long hs[NMAX + 1];
  long long pw[NMAX + 1], invPw[NMAX + 1];

  long long power(long long a, long long b, long long mod) {
    long long ret = 1;
    while (b) {
      if (b & 1) {
        ret = (ret * a) % mod;
      }
      a = (a * a) % mod;
      b /= 2;
    }
    return ret;
  }

  void init(int base, int mod, int n, string& s) {
    this->BASE = base;
    this->MOD = mod;

    long long invBase = power(BASE, MOD - 2, MOD);
    pw[0] = invPw[0] = 1;
    for (int i = 1; i <= n; ++i) {
      pw[i] = (pw[i - 1] * BASE) % MOD;
      invPw[i] = (invPw[i - 1] * invBase) % MOD;
      hs[i] = (hs[i - 1] + 1ll * s[i] * pw[i - 1]) % MOD;
    }
  }

  long long getHash(int l, int r) {
    long long tmp = hs[r] - hs[l - 1];
    if (tmp < 0) {
      tmp += MOD;
    }
    return tmp * invPw[l - 1] % MOD;
  }
};

int n;
string s;
Hash hs1, hs2;

bool ok(int len) {
  if (len == 0) {
    return true;
  }
  set<long long> f;
  for (int i = len; i <= n; ++i) {
    long long tmp = hs1.getHash(i - len + 1, i) * (1e9) + hs2.getHash(i - len + 1, i);
    if (f.count(tmp)) {
      return true;
    }
    f.insert(tmp);
  }
  return false;
}

int main() {
#define taskname "cau3"
  if (fopen (taskname".inp", "r")) {
    freopen (taskname".inp", "r", stdin);
    freopen (taskname".out", "w", stdout);
  }
  ios::sync_with_stdio(false); cin.tie(nullptr);
  cin >> n >> s;
  s = ' ' + s;

  hs1.init(311, 1e9 + 9, n, s);
  hs2.init(317, 1e9 + 9277, n, s);

  int l = 0, r = n + 1;
  while (r - l > 1) {
    int mid = (l + r) >> 1;

    if (ok(mid)) {
      l = mid;
    } else {
      r = mid;
    }
  }
  cout << l << '\n';
  return 0;
}


