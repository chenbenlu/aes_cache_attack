#ifndef AES_H
#define AES_H

#include <stdint.h>

void aes_encrypt(uint8_t *state, const uint8_t *key);
void aes_decrypt(uint8_t *state, const uint8_t *key);
extern const uint8_t sbox[256];
extern const uint8_t inv_sbox[256];
uint64_t rdtscp();
void flush_cache_line(void *addr);

#endif
