#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <time.h>
#include "aes.h"

#define NUM_SAMPLES 1000
#define TARGET_INDEX 0x63  // 你想測試的 sbox 索引（示意）

uint64_t access_times[NUM_SAMPLES];

void attack_timing_test(const uint8_t *key, uint8_t plaintext) {
    uint8_t state[16] = {0};
    state[0] = plaintext;

    for (int i = 0; i < NUM_SAMPLES; i++) {
        // Flush sbox[TARGET_INDEX] cache line
        flush_cache_line((void*)&sbox[TARGET_INDEX]);

        // 加密（單一 byte 變成全 block 這是簡化示意）
        aes_encrypt(state, key);

        // 量測訪問 sbox[TARGET_INDEX] 時間
        uint64_t start = rdtscp();
        volatile uint8_t dummy = sbox[TARGET_INDEX];
        uint64_t end = rdtscp();

        access_times[i] = end - start;
    }
}

int main() {
    uint8_t key[16] = {0x01,0x23,0x45,0x67,0x89,0xAB,0xCD,0xEF,0xFE,0xDC,0xBA,0x98,0x76,0x54,0x32,0x10};
    uint8_t plaintext = 0x00;

    attack_timing_test(key, plaintext);

    // 將時間寫檔給繪圖用
    FILE *f = fopen("cache_times.txt", "w");
    for (int i = 0; i < NUM_SAMPLES; i++) {
        fprintf(f, "%lu\n", access_times[i]);
    }
    fclose(f);

    printf("Timing data saved to cache_times.txt\n");
    return 0;
}
