/*
 *
 * driver for accessing
 * https://www.sainsmart.com/sainsmart-4-channel-5v-usb-relay-board-module-controller-for-automation-robotics.html
 * usb relay with linux.
 *
 * install libftdi drivers
 * http://www.ftdichip.com/Drivers/D2XX.htm
 *
 * ftdi_sio module must be unloaded...
 *
 * http://www.ftdichip.com/Drivers/D2XX.htm
 * may adds a solution
 * tried to make udev rule:
 * /etc/udev/rules.d/60-ftdi_relay.rules
 *
 * compile with:
 * gcc -o simple simple.c -L. -lftd2xx -Wl,-rpath /usr/local/lib
 *
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include "./ftd2xx.h"

#define BUF_SIZE 3

#define MAX_DEVICES		5

// Gloabls
FT_HANDLE ftHandle[MAX_DEVICES];

void quit()
{  
	int i;

	for(i = 0; i < MAX_DEVICES; i++) {
		if(ftHandle[i] != NULL) {
			FT_W32_CloseHandle(ftHandle[i]);
			ftHandle[i] = NULL;
			printf("Closed device\n");
		}
	}

	exit(1);
}

int main(int argc, char **argv)
{
	unsigned char 	data[BUF_SIZE];
	int len;
	int res;
	FT_HANDLE	fthandle;
	int state = 0;
	int mask = 0;
	char current;
	char new;
	char 	cBufWrite[BUF_SIZE];
	char * 	pcBufLD[MAX_DEVICES + 1];
	char 	cBufLD[MAX_DEVICES][64];
	DWORD 	dwBytesWritten, dwBytesRead, dwwritten;
	FT_STATUS	ftStatus;
	int	iNumDevs = 0;
	int	i, j;
		
	for(i = 0; i < MAX_DEVICES; i++) {
		pcBufLD[i] = cBufLD[i];
		ftHandle[i] = NULL;
	}

	pcBufLD[MAX_DEVICES] = NULL;
	
	ftStatus = FT_ListDevices(pcBufLD, &iNumDevs, FT_LIST_ALL | FT_OPEN_BY_SERIAL_NUMBER);
	
	if(ftStatus != FT_OK) {
		printf("Error: FT_ListDevices(%d)\n", ftStatus);
		return 1;
	}
	for(i = 0; ( (i <MAX_DEVICES) && (i < iNumDevs) ); i++) {
		printf("Device %d Serial Number - %s\n", i, cBufLD[i]);
	}

	signal(SIGINT, quit);		// trap ctrl-c call quit fn 

	state = atoi(argv[1]);
	mask = atoi(argv[2]);

	printf("state: %d mask: %d\n", state, mask);
	res = FT_Open(0, &fthandle);
	if (res != FT_OK) {
		printf("RES:%d\n", res);
		return 2;
	}
	ftStatus = FT_SetBaudRate(fthandle, 9600);
	ftStatus = FT_SetBitMode(fthandle, 15, 1);
	len = 1;
	ftStatus = FT_Read(fthandle, &current, 1, &dwBytesRead);
	if (ftStatus != FT_OK) {
		printf("RES:%d\n", res);
		return 3;
	}
	new = (state & mask) | (current & ~mask) & 0xff;
        //printf("READ: st: %d len: %d cur: %x new: %x\n", ftStatus, dwwritten, current, new);
	len = 3;
	data[0] = 0xff;
	data[1] = 0;
	data[2] = new;
	ftStatus = FT_Write(fthandle, &data, len, &dwwritten);
	FT_Close(fthandle);

	return 0;	
}
