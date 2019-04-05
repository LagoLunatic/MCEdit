
.org 0x080AD380
  push r14
  
  mov r0, 0h
  bl LoadSaveFile
  mov r0, 0h
  bl SetCurrentSaveFile
  mov r0, 2h
  bl SetGameState
  
  ; Skip intro (in case this save file has not been started)
  ldr r0,=02002A40h
  mov r1, 10h
  lsl r1, r1, 4h
  strh r1, [r0]
  
  add r0, 88h
  ldr r1,=test_room_data
  ldrb r2, [r1] ; Area index
  strb r2, [r0]
  ldrb r2, [r1,1h] ; Room index
  strb r2, [r0,1h]
  ldrh r2, [r1,2h] ; X pos
  strh r2, [r0,4h]
  ldrh r2, [r1,4h] ; Y pos
  strh r2, [r0,6h]
  
  pop r15
  .pool
.global test_room_data
test_room_data:
  .byte 1
  .byte 0
  .short 0x0080
  .short 0x0060

.org 0x08052C04
  ; Prevent Ezlo from giving a hint when you load in
  b 0x08052C30
