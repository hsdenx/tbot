Environment Variables Commands
------------------------------

printenv- print environment variables
.....................................


::

  => help printenv
  printenv - print environment variables
  
  Usage:
  printenv [-a]
      - print [all] values of all environment variables
  printenv name ...
      - print value of environment variable 'name'
  => 

The :redtext:`printenv` command prints one, several or all variables of the U-Boot environment. When arguments are given, these are interpreted as the names of environment variables which will be printed with their values: 


::

  => printenv ipaddr hostname netmask
  ipaddr=192.168.3.20
  hostname=bbb
  netmask=255.255.255.0
  => 

Without arguments, :redtext:`printenv` prints all a list with all variables in the environment and their values, plus some statistics about the current usage and the total size of the memory available for the environment. 


::

  => printenv
  addcon=setenv bootargs ${bootargs} console=${console}
  addip=setenv bootargs ${bootargs} ip=${ipaddr}:${serverip}:${gatewayip}:${netmask}:${hostname}:${netdev}::off panic=1
  addmisc=setenv bootargs ${bootargs} loglevel=8
  addmtd=setenv bootargs ${bootargs} ${mtdparts}
  arch=arm
  args_mmc=run finduuid;setenv bootargs console=${console} ${optargs} root=PARTUUID=${uuid} rw rootfstype=${mmcrootfstype}
  baudrate=115200
  board=am335x
  board_name=A335BNLT
  board_rev=00C0
  board_serial=414BBBK0180
  boot_a_script=load ${devtype} ${devnum}:${distro_bootpart} ${scriptaddr} ${prefix}${script}; source ${scriptaddr}
  boot_efi_binary=load ${devtype} ${devnum}:${distro_bootpart} ${kernel_addr_r} efi/boot/bootarm.efi; if fdt addr\
    ${fdt_addr_r}; then bootefi ${kernel_addr_r} ${fdt_addr_r};else bootefi ${kernel_addr_r} ${fdtcontroladdr};fi
  boot_extlinux=sysboot ${devtype} ${devnum}:${distro_bootpart} any ${scriptaddr} ${prefix}extlinux/extlinux.conf
  boot_fdt=try
  boot_fit=0
  boot_net_usb_start=usb start
  boot_prefixes=/ /boot/
  boot_script_dhcp=boot.scr.uimg
  boot_scripts=boot.scr.uimg boot.scr
  boot_targets=mmc0 legacy_mmc0 mmc1 legacy_mmc1 nand0 pxe dhcp 
  bootcmd=if test ${boot_fit} -eq 1; then run update_to_fit;fi;run findfdt; run init_console; run envboot; run distro_bootcmd
  bootcmd_dhcp=run boot_net_usb_start; if dhcp ${scriptaddr} ${boot_script_dhcp}; then source ${scriptaddr}; fi;setenv\
    efi_fdtfile ${fdtfile}; if test -z "${fdtfile}" -a -n "${soc}"; then setenv efi_fdtfile ${soc}-${board}${boardver}.dtb; fi;\
    setenv efi_old_vci ${bootp_vci};setenv efi_old_arch ${bootp_arch};setenv bootp_vci PXEClient:Arch:00010:UNDI:003000;setenv\
    bootp_arch 0xa;if dhcp ${kernel_addr_r}; then tftpboot ${fdt_addr_r} dtb/${efi_fdtfile};if fdt addr ${fdt_addr_r}; then\
    bootefi ${kernel_addr_r} ${fdt_addr_r}; else bootefi ${kernel_addr_r} ${fdtcontroladdr};fi;fi;setenv bootp_vci\
    ${efi_old_vci};setenv bootp_arch ${efi_old_arch};setenv efi_fdtfile;setenv efi_old_arch;setenv efi_old_vci;
  bootcmd_legacy_mmc0=setenv mmcdev 0; setenv bootpart 0:2 ; run mmcboot
  bootcmd_legacy_mmc1=setenv mmcdev 1; setenv bootpart 1:2 ; run mmcboot
  bootcmd_mmc0=setenv devnum 0; run mmc_boot
  bootcmd_mmc1=setenv devnum 1; run mmc_boot
  bootcmd_nand=run nandboot
  bootcmd_pxe=run boot_net_usb_start; dhcp; if pxe get; then pxe boot; fi
  bootcount=6
  bootdelay=2
  bootdir=/boot
  bootenvfile=uEnv.txt
  bootfile=beagleboneblack/tbot/zImage
  bootm_size=0x10000000
  bootpart=0:2
  bootscript=echo Running bootscript from mmc${mmcdev} ...; source ${loadaddr}
  cmp_addr_r=82000000
  cmp_mlo=tftp ${cmp_addr_r} ${mlofile};cmp.b ${load_addr_r} ${cmp_addr_r} ${filesize}
  cmp_uboot=tftp ${cmp_addr_r} ${ubfile};cmp.b ${load_addr_r} ${cmp_addr_r} ${filesize}
  console=ttyS0,115200n8
  cpu=armv7
  dfu_alt_info_emmc=rawemmc raw 0 3751936
  dfu_alt_info_mmc=boot part 0 1;rootfs part 0 2;MLO fat 0 1;MLO.raw raw 0x100 0x100;u-boot.img.raw raw 0x300 0x1000;u-env.raw\
    raw 0x1300 0x200;spl-os-args.raw raw 0x1500 0x200;spl-os-image.raw raw 0x1700 0x6900;spl-os-args fat 0 1;spl-os-image fat 0\
    1;u-boot.img fat 0 1;uEnv.txt fat 0 1
  dfu_alt_info_nand=SPL part 0 1;SPL.backup1 part 0 2;SPL.backup2 part 0 3;SPL.backup3 part 0 4;u-boot part 0 5;u-boot-spl-os\
    part 0 6;kernel part 0 8;rootfs part 0 9
  dfu_alt_info_ram=kernel ram 0x80200000 0x4000000;fdt ram 0x80f80000 0x80000;ramdisk ram 0x81000000 0x4000000
  distro_bootcmd=for target in ${boot_targets}; do run bootcmd_${target}; done
  efi_dtb_prefixes=/ /dtb/ /dtb/current/
  envboot=mmc dev ${mmcdev}; if mmc rescan; then echo SD/MMC found on device ${mmcdev};if run loadbootscript; then run\
    bootscript;else if run loadbootenv; then echo Loaded env from ${bootenvfile};run importbootenv;fi;if test -n $uenvcmd; then\
    echo Running uenvcmd ...;run uenvcmd;fi;fi;fi;
  eth1addr=6c:ec:eb:83:40:33
  ethaddr=6c:ec:eb:83:40:31
  fdt_addr_r=0x88000000
  fdtaddr=0x88000000
  fdtcontroladdr=9df21ed8
  fdtfile=beagleboneblack/tbot/am335x-boneblack.dtb
  filesize=b2ee8
  findfdt=if test $board_name = A335BONE; then setenv fdtfile am335x-bone.dtb; fi; if test $board_name = A335BNLT; then setenv\
    fdtfile am335x-boneblack.dtb; fi; if test $board_name = BBBW; then setenv fdtfile am335x-boneblack-wireless.dtb; fi; if test\
    $board_name = BBG1; then setenv fdtfile am335x-bonegreen.dtb; fi; if test $board_name = BBGW; then setenv fdtfile am335x-\
    bonegreen-wireless.dtb; fi; if test $board_name = BBBL; then setenv fdtfile am335x-boneblue.dtb; fi; if test $board_name =\
    A33515BB; then setenv fdtfile am335x-evm.dtb; fi; if test $board_name = A335X_SK; then setenv fdtfile am335x-evmsk.dtb; fi;\
    if test $board_name = A335_ICE; then setenv fdtfile am335x-icev2.dtb; fi; if test $fdtfile = undefined; then echo WARNING:\
    Could not determine device tree to use; fi;
  finduuid=part uuid mmc ${bootpart} uuid
  fit_bootfile=fitImage
  fit_loadaddr=0x87000000
  hostname=bbb
  importbootenv=echo Importing environment from mmc${mmcdev} ...; env import -t ${loadaddr} ${filesize}
  init_console=if test $board_name = A335_ICE; then setenv console ttyO3,115200n8;else setenv console ttyO0,115200n8;fi;
  ipaddr=192.168.3.20
  kernel_addr_r=0x82000000
  load_addr_r=81000000
  load_efi_dtb=load ${devtype} ${devnum}:${distro_bootpart} ${fdt_addr_r} ${prefix}${efi_fdtfile}
  load_mlo=tftp ${load_addr_r} ${mlofile}
  load_uboot=tftp ${load_addr_r} ${ubfile}
  loadaddr=0x82000000
  loadbootenv=fatload mmc ${mmcdev} ${loadaddr} ${bootenvfile}
  loadbootscript=load mmc ${mmcdev} ${loadaddr} boot.scr
  loadfdt=load ${devtype} ${bootpart} ${fdtaddr} ${bootdir}/${fdtfile}
  loadfit=run args_mmc; bootm ${loadaddr}#${fdtfile};
  loadimage=load ${devtype} ${bootpart} ${loadaddr} ${bootdir}/${bootfile}
  loadramdisk=load mmc ${mmcdev} ${rdaddr} ramdisk.gz
  mlofile=beagleboneblack/tbot/MLO
  mmc_boot=if mmc dev ${devnum}; then setenv devtype mmc; run scan_dev_for_boot_part; fi
  mmc_mmc=run mmcloadk; run mmcloadfdt;run args_mmc;bootz ${loadaddr} - ${fdtaddr}
  mmcboot=mmc dev ${mmcdev}; setenv devnum ${mmcdev}; setenv devtype mmc; if mmc rescan; then echo SD/MMC found on device\
    ${mmcdev};if run loadimage; then if test ${boot_fit} -eq 1; then run loadfit; else run mmcloados;fi;fi;fi;
  mmcdev=0
  mmcloadfdt=ext2load mmc 0:2 ${fdtaddr} /boot/am335x-boneblack.dtb
  mmcloadk=ext2load mmc 0:2 ${loadaddr} /boot/zImage
  mmcloados=run args_mmc; if test ${boot_fdt} = yes || test ${boot_fdt} = try; then if run loadfdt; then bootz ${loadaddr} -\
    ${fdtaddr}; else if test ${boot_fdt} = try; then bootz; else echo WARN: Cannot load the DT; fi; fi; else bootz; fi;
  mmcrootfstype=ext4 rootwait
  mtdids=nand0=nand.0
  mtdparts=mtdparts=nand.0:128k(NAND.SPL),128k(NAND.SPL.backup1),128k(NAND.SPL.backup2),128k(NAND.SPL.backup3),256k(NAND.u\
    -boot-spl-os),1m(NAND.u-boot),128k(NAND.u-boot-env),128k(NAND.u-boot-env.backup1),8m(NAND.kernel),-(NAND.file-system)
  nandargs=setenv bootargs console=${console} ${optargs} root=${nandroot} rootfstype=${nandrootfstype}
  nandboot=echo Booting from nand ...; run nandargs; nand read ${fdtaddr} NAND.u-boot-spl-os; nand read ${loadaddr}\
    NAND.kernel; bootz ${loadaddr} - ${fdtaddr}
  nandroot=ubi0:rootfs rw ubi.mtd=NAND.file-system,2048
  nandrootfstype=ubifs rootwait=1
  net_nfs=run netloadimage; run netloadfdt;run nfsargs addcon addip addmtd addmisc;bootz ${loadaddr} - ${fdtaddr}
  netargs=setenv bootargs console=${console} ${optargs} root=/dev/nfs nfsroot=${serverip}:${rootpath},${nfsopts} rw ip=dhcp
  netboot=echo Booting from network ...; setenv autoload no; dhcp; run netloadimage; run netloadfdt; run netargs; bootz\
    ${loadaddr} - ${fdtaddr}
  netdev=eth0
  netloadfdt=tftp ${fdtaddr} ${fdtfile}
  netloadimage=tftp ${loadaddr} ${bootfile}
  netmask=255.255.255.0
  netmmcboot=echo Booting from network ... with mmcargs ...; setenv autoload no; run netloadimage; run netloadfdt; run\
    args_mmc; bootz ${loadaddr} - ${fdtaddr}
  nfsargs=setenv bootargs ${bootargs} root=/dev/nfs rw nfsroot=${serverip}:${rootpath},${nfsopts}
  nfsopts=nfsvers=3 nolock rw
  partitions=uuid_disk=${uuid_gpt_disk};name=rootfs,start=2MiB,size=-,uuid=${uuid_gpt_rootfs}
  pxefile_addr_r=0x80100000
  ramargs=setenv bootargs console=${console} ${optargs} root=${ramroot} rootfstype=${ramrootfstype}
  ramboot=echo Booting from ramdisk ...; run ramargs; bootz ${loadaddr} ${rdaddr} ${fdtaddr}
  ramdisk_addr_r=0x88080000
  ramroot=/dev/ram0 rw
  ramrootfstype=ext2
  rdaddr=0x88080000
  rootpath=/work/tbot2go/tbot/nfs/bbb
  scan_dev_for_boot=echo Scanning ${devtype} ${devnum}:${distro_bootpart}...; for prefix in ${boot_prefixes}; do run\
    scan_dev_for_extlinux; run scan_dev_for_scripts; done;run scan_dev_for_efi;
  scan_dev_for_boot_part=part list ${devtype} ${devnum} -bootable devplist; env exists devplist || setenv devplist 1; for\
    distro_bootpart in ${devplist}; do if fstype ${devtype} ${devnum}:${distro_bootpart} bootfstype; then run scan_dev_for_boot;\
    fi; done
  scan_dev_for_efi=setenv efi_fdtfile ${fdtfile}; if test -z "${fdtfile}" -a -n "${soc}"; then setenv efi_fdtfile\
    ${soc}-${board}${boardver}.dtb; fi; for prefix in ${efi_dtb_prefixes}; do if test -e ${devtype} ${devnum}:${distro_bootpart}\
    ${prefix}${efi_fdtfile}; then run load_efi_dtb; fi;done;if test -e ${devtype} ${devnum}:${distro_bootpart}\
    efi/boot/bootarm.efi; then echo Found EFI removable media binary efi/boot/bootarm.efi; run boot_efi_binary; echo EFI LOAD\
    FAILED: continuing...; fi; setenv efi_fdtfile
  scan_dev_for_extlinux=if test -e ${devtype} ${devnum}:${distro_bootpart} ${prefix}extlinux/extlinux.conf; then echo Found\
    ${prefix}extlinux/extlinux.conf; run boot_extlinux; echo SCRIPT FAILED: continuing...; fi
  scan_dev_for_scripts=for script in ${boot_scripts}; do if test -e ${devtype} ${devnum}:${distro_bootpart} ${prefix}${script};\
    then echo Found U-Boot script ${prefix}${script}; run boot_a_script; echo SCRIPT FAILED: continuing...; fi; done
  scriptaddr=0x80000000
  serverip=192.168.3.1
  soc=am33xx
  spiargs=setenv bootargs console=${console} ${optargs} root=${spiroot} rootfstype=${spirootfstype}
  spiboot=echo Booting from spi ...; run spiargs; sf probe ${spibusno}:0; sf read ${loadaddr} ${spisrcaddr} ${spiimgsize};\
    bootz ${loadaddr}
  spibusno=0
  spiimgsize=0x362000
  spiroot=/dev/mtdblock4 rw
  spirootfstype=jffs2
  spisrcaddr=0xe0000
  static_ip=${ipaddr}:${serverip}:${gatewayip}:${netmask}:${hostname}::off
  stderr=serial@44e09000
  stdin=serial@44e09000
  stdout=serial@44e09000
  tbot_cmp_spl=run cmp_mlo
  tbot_cmp_uboot=run cmp_uboot
  tbot_upd_spl=run load_mlo;run upd_mlo
  tbot_upd_uboot=run load_uboot;run upd_uboot
  ubfile=beagleboneblack/tbot/u-boot.img
  upd_mlo=fatwrite mmc 1:1 ${load_addr_r} mlo ${filesize}
  upd_uboot=fatwrite mmc 1:1 ${load_addr_r} u-boot.img ${filesize}
  update_to_fit=setenv loadaddr ${fit_loadaddr}; setenv bootfile ${fit_bootfile}
  usb_boot=usb start; if usb dev ${devnum}; then setenv devtype usb; run scan_dev_for_boot_part; fi
  vendor=ti
  ver=U-Boot 2017.09-00396-g6ca43a5 (Sep 30 2017 - 07:16:03 +0200)
  
  Environment size: 11032/131068 bytes
  => 

saveenv - save environment variables to persistent storage
..........................................................


::

  => help saveenv
  saveenv - save environment variables to persistent storage
  
  Usage:
  saveenv 
  => 

All changes you make to the U-Boot environment are made in RAM only. They are lost as soon as you reboot the system. If you want to make your changes permanent you have to use the :redtext:`saveenv` command to write a copy of the environment settings to persistent storage, from where they are automatically loaded during startup: 


::

  => saveenv
  Saving Environment to FAT...
  writing uboot.env
  FAT: Misaligned buffer address (9df01d58)
  done
  => 

setenv - set environment variables
..................................


::

  => help setenv
  setenv - set environment variables
  
  Usage:
  setenv [-f] name value ...
      - [forcibly] set environment variable 'name' to 'value ...'
  setenv [-f] name
      - [forcibly] delete environment variable 'name'
  => 

To modify the U-Boot environment you have to use the :redtext:`setenv` command. When called with exactly one argument, it will delete any variable of that name from U-Boot's environment, if such a variable exists. Any storage occupied for such a variable will be automatically reclaimed: 


::

  => setenv foo This is an example value.
  => printenv foo
  foo=This is an example value.
  => setenv foo
  => printenv foo
  ## Error: "foo" not defined
  => 

When called with more arguments, the first one will again be the name of the variable, and all following arguments will (concatenated by single space characters) form the value that gets stored for this variable. New variables will be automatically created, existing ones overwritten. 


::

  => printenv bar
  ## Error: "bar" not defined
  => setenv bar This is a new example.
  => printenv bar
  bar=This is a new example.
  => setenv bar
  => 

Remember standard shell quoting rules when the value of a variable shall contain characters that have a special meaning to the command line parser (like the $ character that is used for variable substitution or the semicolon which separates commands). Use the backslash (\) character to escape such special characters, or enclose the whole phrase in apstrophes ('). Use "${name}" for variable expansion. 


::

  => setenv cons_opts 'console=tty0 console=ttyS0,\${baudrate}'
  => printenv cons_opts
  cons_opts=console=tty0 console=ttyS0,${baudrate}
  => setenv cons_opts
  => 

|Help| There is no restriction on the characters that can be used in a variable name except the restrictions imposed by the command line parser (like using backslash for quoting, space and tab characters to separate arguments, or semicolon and newline to separate commands). Even strange input like :redtext:`=-/|()+=` is a perfectly legal variable name in U-Boot. 

|Warning| A common mistake is to write 

::

  setenv name=value

instead of

::

  setenv name value

There will be no error message, which lets you believe everything went OK, but it didn't: instead of setting the variable name to the value value you tried to delete a variable with the name name=value - this is probably not what you intended! Always remember that name and value have to be separated by space and/or tab characters! 
