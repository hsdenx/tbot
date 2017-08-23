mw - memory write (fill)
........................


::

  => help mw
  mw - memory write (fill)
  
  Usage:
  mw [.b, .w, .l] address value [count]
  => 

The :redtext:`mw` command is a way to initialize (fill) memory with some value. When called without a count argument, the value will be written only to the specified address. When used with a count value, the entire memory area will be initialized with this value: 


::

  => md 0x80000000 0x10
  80000000: 6c6c6548 2020206f 01234567 01fbbcc3    Hello   gE#.....
  80000010: 89e9712a 0fb40e16 6f236743 3b46fbe6    *q......Cg#o..F;
  80000020: ea2356f6 6e7c540f e056e377 7bd28a9f    .V#..T|nw.V....{
  80000030: cfa9bcec b19ace51 b27f4dc5 8eeca28b    ....Q....M......
  => mw 0x80000000 0xaabbccdd
  => md 0x80000000 0x10
  80000000: aabbccdd 2020206f 01234567 01fbbcc3    ....o   gE#.....
  80000010: 89e9712a 0fb40e16 6f236743 3b46fbe6    *q......Cg#o..F;
  80000020: ea2356f6 6e7c540f e056e377 7bd28a9f    .V#..T|nw.V....{
  80000030: cfa9bcec b19ace51 b27f4dc5 8eeca28b    ....Q....M......
  => mw 0x80000000 0 6
  => md 0x80000000 0x10
  80000000: 00000000 00000000 00000000 00000000    ................
  80000010: 00000000 00000000 6f236743 3b46fbe6    ........Cg#o..F;
  80000020: ea2356f6 6e7c540f e056e377 7bd28a9f    .V#..T|nw.V....{
  80000030: cfa9bcec b19ace51 b27f4dc5 8eeca28b    ....Q....M......
  => 

This is another command that accepts the type extensions :redtext:`.l`, :redtext:`.w` and :redtext:`.b` :


::

  => mw.w 0x80000004 0x1155 6
  => md 0x80000000 0x10
  80000000: 00000000 11551155 11551155 11551155    ....U.U.U.U.U.U.
  80000010: 00000000 00000000 6f236743 3b46fbe6    ........Cg#o..F;
  80000020: ea2356f6 6e7c540f e056e377 7bd28a9f    .V#..T|nw.V....{
  80000030: cfa9bcec b19ace51 b27f4dc5 8eeca28b    ....Q....M......
  => mw.b 0x80000007 0xff 7
  => md 0x80000000 0x10
  80000000: 00000000 ff551155 ffffffff 1155ffff    ....U.U.......U.
  80000010: 00000000 00000000 6f236743 3b46fbe6    ........Cg#o..F;
  80000020: ea2356f6 6e7c540f e056e377 7bd28a9f    .V#..T|nw.V....{
  80000030: cfa9bcec b19ace51 b27f4dc5 8eeca28b    ....Q....M......
  => 

