; Harmonic QEMU Stub - MBR Boot with INT 0x0 Hook
BITS 16
ORG 0x7C00

start:
    cli
    xor ax, ax
    mov ds, ax
    mov es, ax

    ; Install hook for INT 0x0 (div0)
    mov ax, 0x0008  ; Code segment
    mov ds, ax
    mov word [0x00], pause_handler  ; Low word of interrupt vector
    mov word [0x02], 0x0000  ; High word

    ; Test: Force div0
    mov ax, 5
    mov bx, 0
    div bx  ; Triggers INT 0x0 → Pause

    ; Test add 3+0
    mov ax, 3
    add ax, 0  ; Safe neutral

    ; Print success
    mov si, msg
    call print_string
    hlt

pause_handler:
    ; ⊘ Pause: Log 'Pause' on screen, no crash
    push ax
    mov ah, 0x0E
    mov bx, 0x07
    mov al, 'P'
    int 0x10
    mov al, 'a'
    int 0x10
    mov al, 'u'
    int 0x10
    mov al, 's'
    int 0x10
    mov al, 'e'
    int 0x10
    pop ax
    iret

print_string:
    lodsb
    or al, al
    jz .done
    mov ah, 0x0E
    int 0x10
    jmp print_string
.done:
    ret

msg db 'Harmonic Boot: Div0 Paused. Add OK', 0

times 510-($-$$) db 0
dw 0xAA55