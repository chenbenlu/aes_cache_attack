#include <stdio.h>
#include <string.h>
#include "aes.h"

void print_block(const char *label, const uint8_t *block) {
    printf("%s: ", label);
    for (int i = 0; i < 16; ++i)
        printf("%02X ", block[i]);
    printf("\n");
}

int main() {
    uint8_t plaintext[16]  = "MemorySystem2025";
    uint8_t ciphertext[16];
    uint8_t decrypted[16];
    uint8_t key[16]        = {0x2F};

    memcpy(ciphertext, plaintext, 16);
    aes_encrypt(ciphertext, key);
    memcpy(decrypted, ciphertext, 16);
    aes_decrypt(decrypted, key);

    print_block("Plaintext ", plaintext);
    print_block("Ciphertext", ciphertext);
    print_block("Decrypted ", decrypted);

    // 測量特定 sbox 項的存取時間（模擬 flush+reload）
    uint8_t *target = (uint8_t *)&sbox[0x63];
    flush_cache_line(target);
    uint64_t t1 = rdtscp();
    volatile uint8_t x = *target;
    uint64_t t2 = rdtscp();

    printf("Access time to sbox[0x63] after flush: %lu cycles\n", t2 - t1);
    return 0;
}
