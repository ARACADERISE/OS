org 0x7C00
bits 16

jmp 0x0000:init

init:
	xor ax, ax
	mov dx, ax
	mov cx, ax

cli
mov bp, 0x7C00
mov ss, ax
mov sp, bp
sti

load:
	mov ax, 0x07E0
	mov es, ax
	xor bx, bx
	
	mov al, 0x01
	mov cl, [SECTOR_START]

.loop:
	mov ah, 0x04
	mov ch, 0x00
	mov dh, 0x00
	mov dl, [BOOT_DRIVE]
	int 0x13

	cmp ah, 0x00
	jne failed

	mov ah, 0x00
	mov dl, 0x80
	int 0x13

	mov ah, 0x02
	mov ch, 0x00
	mov dh, 0x00
	mov dl, [BOOT_DRIVE]
	int 0x13

	jc failed

	cmp ah, 0x00
	jne failed
	cmp al, 0x00
	je failed

	cmp cl, [SECTORS_TO_READ]
	je done
	
	add cl, 1
	jmp .loop

done:

	mov ah, 0x0e
	mov al, 'D'
	int 0x10

	cli
	xor ax, ax
	mov ds, ax
	lgdt [gdt_desc]
	mov eax, cr0
	or eax, 1
	mov cr0, eax

jmp $

gdt:
	null_seg: dq 0
	code_seg:
		dw 0xFFFF
		dw 0x0
		db 0
		db 10011010b
		db 11001111b
		db 0
	gdt_data:
		dw 0xFFFF
		dw 0x0
		db 0
		db 10010010b
		db 11001111b
		db 0
	gdt_end:
		gdt_desc:
			db gdt_end - gdt
			dw gdt

failed:
	mov ah, 0x0e
	mov al, 'E'
	int 0x10

	jmp $

SECTOR_START dd 0x0002
SECTORS_TO_READ dd 0x0021
BOOT_DRIVE dd 0x0080

times 510 - ($ - $$) db 0
dw 0xaa55

times 16384 db 0
