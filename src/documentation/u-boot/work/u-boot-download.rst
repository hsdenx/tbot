Download Commands
-----------------

bootp - boot image via network using BOOTP/TFTP protocol
........................................................


::

  => help bootp
  bootp - boot image via network using BOOTP/TFTP protocol
  
  Usage:
  bootp [loadAddress] [[hostIPaddr:]bootfilename]
  => 

dhcp - invoke DHCP client to obtain IP/boot params
..................................................


::

  => help dhcp
  dhcp - boot image via network using DHCP/TFTP protocol
  
  Usage:
  dhcp [loadAddress] [[hostIPaddr:]bootfilename]
  => 

.. raw:: pdf

   PageBreak

loadb - load binary file over serial line (kermit mode)
.......................................................


::

  => help loadb
  loadb - load binary file over serial line (kermit mode)
  
  Usage:
  loadb [ off ] [ baud ]
      - load binary file over serial line with offset 'off' and baudrate 'baud'
  => 

With kermit you can download binary data via the serial line.

Make sure you use the following settings in kermit.


::

  set carrier-watch off
  (/work/tbot2go/tbot/) C-Kermit>set handshake none
  (/work/tbot2go/tbot/) C-Kermit>set flow-control none
  (/work/tbot2go/tbot/) C-Kermit>robust
  (/work/tbot2go/tbot/) C-Kermit>set file type bin
  (/work/tbot2go/tbot/) C-Kermit>set file name lit
  (/work/tbot2go/tbot/) C-Kermit>set rec pack 100
  (/work/tbot2go/tbot/) C-Kermit>set send pack 100
  (/work/tbot2go/tbot/) C-Kermit>set window 5
  (/work/tbot2go/tbot/) C-Kermit>

If you have problems with downloading, may you set the values

::

  set rec pack
  set send pack

to smaller values.

Now for example download u-boot.img.


::

  => loadb 80000000
  ## Ready for binary (kermit) download to 0x80000000 at 115200 bps...
  
  (Back at raspberrypitbot2go)
  ----------------------------------------------------
  (/work/tbot2go/tbot/) C-Kermit>
  (/work/tbot2go/tbot/) C-Kermit>send /protocol=kermit /srv/tftpboot//beagleboneblack/tbot/u-boot.img                     
  C-Kermit 9.0.302 OPEN SOURCE:, 20 Aug 2011, raspberrypitbot2go [192.168.3.1]                                            
                                                                                                                          
     Current Directory: /work/tbot2go/tbot                                                                                
  Communication Parity: none/ttyUSB0                                                                                      
   CommunicRTT/Timeout: 01 / 02                                                                                           
               SENDING:  => /tftpboot//beagleboneblack/tbot/u-boot.img                                                    
             File Type: BINARY                                                                                            
             File Size: 732904                                                                                            
          Percent Done: 100 //////////////////////////////////////////////////                                            
  :06  ...10...20...30...40...50...60...70...80...90..100                                                              :01
          Elapsed Time: 00:02:33                                                                                          
  76Transfer Rate, CPS: 4704                                                                                             0
  550     Window Slots: 1 of 1                                                                                        %767
  332      Packet Type: B                                                                                          2105674
  3108    Packet Count: 53006                                                                                         1226
                                                                                                                          
  hecksum errorr Count: 84                                                                                              (r
  esend)                                                                                                                  
          Last Message: SUCCESS.  Files: 1, Bytes: 732904, 4787 CPS                                                       
                                                                                                                          
                                                                                                                          
  (/work/tbot2go/tbot/) C-Kermit>connect                                                                                  
  Connecting to /dev/ttyUSB0, speed 115200                                                                                
   Escape character: Ctrl-\ (ASCII 28, FS): enabled                                                                       
  Type the escape character followed by C to get back,                                                                    
  or followed by ? to see other options.                                                                                  
  ----------------------------------------------------                                                                    
  CACHE: Misaligned operation at range [80000000, 800b2ee8]                                                               
  ## Total Size      = 0x000b2ee8 = 732904 Bytes                                                                          
  ## Start Addr      = 0x80000000                                                                                         
  =>                                                                                                                      
                                                                                                                          

  => imi 80000000
  
  ## Checking Image at 80000000 ...
     FIT image found
     FIT description: Firmware image with one or more FDT blobs
     Created:         2017-09-30   5:16:48 UTC
      Image 0 (firmware@1)
       Description:  U-Boot 2017.09-00396-g6ca43a5 for am335x board
       Created:      2017-09-30   5:16:48 UTC
       Type:         Firmware
       Compression:  uncompressed
       Data Start:   unavailable
       Data Size:    unavailable
       Architecture: ARM
       Load Address: 0x80800000
      Image 1 (fdt@1)
       Description:  am335x-evm
       Created:      2017-09-30   5:16:48 UTC
       Type:         Firmware
       Compression:  uncompressed
       Data Start:   unavailable
       Data Size:    unavailable
       Architecture: ARM
       Load Address: unavailable
      Image 2 (fdt@2)
       Description:  am335x-bone
       Created:      2017-09-30   5:16:48 UTC
       Type:         Firmware
       Compression:  uncompressed
       Data Start:   unavailable
       Data Size:    unavailable
       Architecture: ARM
       Load Address: unavailable
      Image 3 (fdt@3)
       Description:  am335x-boneblack
       Created:      2017-09-30   5:16:48 UTC
       Type:         Firmware
       Compression:  uncompressed
       Data Start:   unavailable
       Data Size:    unavailable
       Architecture: ARM
       Load Address: unavailable
      Image 4 (fdt@4)
       Description:  am335x-evmsk
       Created:      2017-09-30   5:16:48 UTC
       Type:         Firmware
       Compression:  uncompressed
       Data Start:   unavailable
       Data Size:    unavailable
       Architecture: ARM
       Load Address: unavailable
      Image 5 (fdt@5)
       Description:  am335x-bonegreen
       Created:      2017-09-30   5:16:48 UTC
       Type:         Firmware
       Compression:  uncompressed
       Data Start:   unavailable
       Data Size:    unavailable
       Architecture: ARM
       Load Address: unavailable
      Image 6 (fdt@6)
       Description:  am335x-icev2
       Created:      2017-09-30   5:16:48 UTC
       Type:         Firmware
       Compression:  uncompressed
       Data Start:   unavailable
       Data Size:    unavailable
       Architecture: ARM
       Load Address: unavailable
      Default Configuration: 'conf@1'
      Configuration 0 (conf@1)
       Description:  am335x-evm
       Kernel:       unavailable
       FDT:          fdt@1
      Configuration 1 (conf@2)
       Description:  am335x-bone
       Kernel:       unavailable
       FDT:          fdt@2
      Configuration 2 (conf@3)
       Description:  am335x-boneblack
       Kernel:       unavailable
       FDT:          fdt@3
      Configuration 3 (conf@4)
       Description:  am335x-evmsk
       Kernel:       unavailable
       FDT:          fdt@4
      Configuration 4 (conf@5)
       Description:  am335x-bonegreen
       Kernel:       unavailable
       FDT:          fdt@5
      Configuration 5 (conf@6)
       Description:  am335x-icev2
       Kernel:       unavailable
       FDT:          fdt@6
  ## Checking hash(es) for FIT Image at 80000000 ...
     Hash(es) for Image 0 (firmware@1):  error!
  Can't get image data/size for '' hash node in 'firmware@1' image node
  Bad hash in FIT image!
  => 


.. raw:: pdf

   PageBreak

loads - load S-Record file over serial line
...........................................


::

  => help loads
  loads - load S-Record file over serial line
  
  Usage:
  loads [ off ]
      - load S-Record file over serial line with offset 'off'
  => 

rarpboot- boot image via network using RARP/TFTP protocol
.........................................................


::

  => help rarp
  Unknown command 'rarp' - try 'help' without arguments for list of all known commands
  
  => 

tftpboot- boot image via network using TFTP protocol
....................................................


::

  => help tftp
  tftpboot - boot image via network using TFTP protocol
  
  Usage:
  tftpboot [loadAddress] [[hostIPaddr:]bootfilename]
  => 
