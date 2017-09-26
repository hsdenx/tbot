U-Boot pytest suite
-------------------

Read more of how to setup test/py in U-Boot source code:

http://git.denx.de/?p=u-boot.git;a=blob;f=test/py/README.md

Test py results
...............


::

  $ PATH=/home/hs/data/Entwicklung/test_py_scripts/hook-scripts:$PATH;PYTHONPATH=/work/hs/tb
  ot/u-boot-am335x_evm;./test/py/test.py --bd am335x_evm -s --build-dir .                                                 
  +u-boot-test-flash am335x_evm na                                                                                        
  board type  am335x_evm                                                                                                  
  No flashing supported yet                                                                                               
  ========================================================================================= test session starts ==========
  ================================================================================                                        
  platform linux2 -- Python 2.7.8, pytest-3.2.1, py-1.4.34, pluggy-0.4.0                                                  
  rootdir: $TBOT_BASEDIR/u-boot-am335x_evm/test/py, inifile: pytest.ini                                                   
  collecting 0 items                                                                                                      
  collecting 1 item                                                                                                       
  [...]
  Unknown command 'non_existent_cmd' - try 'help'                                                                         
  =>                                                                                                                      
  test/py/tests/test_unknown_cmd.py .                                                                                     
  test/py/tests/test_ut.py ss                                                                                             
  test/py/tests/test_vboot.py s                                                                                           
                                                                                                                          
  ================================================================================ 74 passed, 20 skipped in 12.71 seconds 
  ================================================================================                                        
  $                                                                                         

