AES Cache Timing Attack

這個專案展示了針對 AES 加密演算法的 Cache Timing Attack。它利用 CPU 快取記憶體存取時間的差異，來推斷 AES 密鑰的秘密資訊。
總覽

當 AES 軟體實作使用查閱表 (如 S-box 或 T-box) 時，快取命中 (快速) 和快取失效 (慢速) 會產生時間差異。攻擊者透過精確測量加密時間，分析這些時間模式，進而推斷出被存取的查閱表條目，並從中還原部分或全部的密鑰。

這個實作採用 Flush+Reload 或 Prime+Probe 策略，攻擊 AES 加密的第一個密鑰位元組。
功能特色

    簡化版 AES 實作：使用查閱表，易受時間攻擊。
    精確計時：使用 RDTSC 指令測量 CPU 週期。
    快取操作：包含清除 (Flush/Evict) 和測量 (Reload/Probe) 快取時間的函數。
    密鑰還原：透過分析時間數據，嘗試還原 AES 密鑰的第一個位元組。

使用指南
編譯

請確保您在 Linux 環境下使用 GCC/Clang 編譯器。
Bash

git clone https://github.com/chenbenlu/aes_cache_attack.git
cd aes_cache_attack
gcc -o aes_attack aes_attack.c -O3 -Wall -march=native -lrt

執行
Bash

./aes_attack

程式將執行多次 AES 加密，測量 S-box 的存取時間，並嘗試推斷密鑰。
