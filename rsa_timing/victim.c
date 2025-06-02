#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>

int modexp(int base, int exp, int mod) {
    int result = 1;
    base = base % mod;

    while (exp > 0) {
        result = (result * result) % mod;  // always square

        if (exp & 1) {
            result = (result * base) % mod;  // this causes timing difference
        }
        exp = exp >> 1;
    }
    return result;
}

// 模擬 victim：讀一個明文 m，回傳其私鑰解密（使用私鑰 d）
int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <message>\n", argv[0]);
        return 1;
    }

    int m = atoi(argv[1]);

    // 固定 RSA 私鑰參數
    int d = 173;      // 私鑰 (需小一點，便於觀察)
    int n = 3233;     // n = p * q = 61 * 53

    // 假裝做解密
    int decrypted = modexp(m, d, n);
    printf("%d\n", decrypted);
    return 0;
}
