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
  80000000: 6c6c6548 2020206f 01234567 dfb0e082    Hello   gE#.....
  80000010: 0d838660 e04e09df 62a2cc8a def1601a    `.....N....b.`..
  80000020: 65b8b965 fb0fa81b c202c517 7fc93243    e..e........C2..
  80000030: d5246ead 92d57185 768d30c9 cecb8383    .n$..q...0.v....
  => mw 0x80000000 0xaabbccdd
  => md 0x80000000 0x10
  80000000: aabbccdd 2020206f 01234567 dfb0e082    ....o   gE#.....
  80000010: 0d838660 e04e09df 62a2cc8a def1601a    `.....N....b.`..
  80000020: 65b8b965 fb0fa81b c202c517 7fc93243    e..e........C2..
  80000030: d5246ead 92d57185 768d30c9 cecb8383    .n$..q...0.v....
  => mw 0x80000000 0 6
  => md 0x80000000 0x10
  80000000: 00000000 00000000 00000000 00000000    ................
  80000010: 00000000 00000000 62a2cc8a def1601a    ...........b.`..
  80000020: 65b8b965 fb0fa81b c202c517 7fc93243    e..e........C2..
  80000030: d5246ead 92d57185 768d30c9 cecb8383    .n$..q...0.v....
  => 

This is another command that accepts the type extensions :redtext:`.l`, :redtext:`.w` and :redtext:`.b` :


::

  => mw.w 0x80000004L 0x1155 6
  => md 0x80000000 0x10
  80000000: 00000000 11551155 11551155 11551155    ....U.U.U.U.U.U.
  80000010: 00000000 00000000 62a2cc8a def1601a    ...........b.`..
  80000020: 65b8b965 fb0fa81b c202c517 7fc93243    e..e........C2..
  80000030: d5246ead 92d57185 768d30c9 cecb8383    .n$..q...0.v....
  => mw.b 0x80000007L 0xff 7
  => md 0x80000000 0x10
  80000000: 00000000 ff551155 ffffffff 1155ffff    ....U.U.......U.
  80000010: 00000000 00000000 62a2cc8a def1601a    ...........b.`..
  80000020: 65b8b965 fb0fa81b c202c517 7fc93243    e..e........C2..
  80000030: d5246ead 92d57185 768d30c9 cecb8383    .n$..q...0.v....
  => 

