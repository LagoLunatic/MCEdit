
.org 0x080AD380
  push r4, r14
  
  ldr r4,=test_room_data
  
  ldrb r0, [r4] ; Save slot
  bl LoadSaveFile
  ldrb r0, [r4] ; Save slot
  bl SetCurrentSaveFile
  mov r0, 2h
  bl SetGameState
  
  ; Skip intro (in case this save file has not been started)
  ldr r0,=02002A40h
  mov r1, 10h
  lsl r1, r1, 4h
  strh r1, [r0]
  
  add r0, 88h
  ldrb r2, [r4,1h] ; Area index
  strb r2, [r0]
  ldrb r2, [r4,2h] ; Room index
  strb r2, [r0,1h]
  ldrh r2, [r4,4h] ; X pos
  strh r2, [r0,4h]
  ldrh r2, [r4,6h] ; Y pos
  strh r2, [r0,6h]
  
  pop r4, r15
  .pool
.global test_room_data
test_room_data:
  .byte 0 ; Save slot
  .byte 1 ; Area index
  .byte 0 ; Room index
  .byte 0 ; Padding so the following variables are halfword aligned
  .short 0x0080 ; X pos
  .short 0x0060 ; Y pos

.org 0x08052C04
  ; Prevent Ezlo from giving a hint when you load in
  b 0x08052C30
