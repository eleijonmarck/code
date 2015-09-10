// -*- C -*-

#ifndef __util_h__
#define __util_h__ 1

#include <stdio.h>

typedef int  i32;
typedef long i64;

typedef unsigned char  u8;
typedef unsigned short u16;
typedef unsigned int   u32;
typedef unsigned long  u64;

static const u64 NSEC_PER_SEC  = 1000000000;
//////////////////////////////////////////////////////////////////////

typedef struct
{
   dl_list list [1];

   u64 order_id;
   u32 instr_id;

   u32 buy_sell;

   u64 price;
   u64 volume;

} order_entry_t;

//////////////////////////////////////////////////////////////////////

int read_msg  (void* data, int size);
int write_msg (const void* data, int size);
#endif // __util_h__

