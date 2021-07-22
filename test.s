org 0x7c00
bits 16

mov si, ax

times 510 - ($ - $$) db 0
dw 0xaa55
