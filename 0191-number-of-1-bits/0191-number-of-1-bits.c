int hammingWeight(uint32_t n) {
    uint32_t c;

    // takes 0 ms to execute
    for(c =0; n; c++) {
        n = n & (n-1);
    }

    // takes 5 ms to execute
    /*for(int i=0; i<32; i++) {
        if ((n>>i)&0x01 == 1) {
            c++;
        }
    }*/ 

    return c;
}