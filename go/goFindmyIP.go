package main

import (
	"fmt"
	"net/http"
	"strings"
	"bufio"
	"os"
	)

func main() {
	ip,err := findMyIP("http://myexternalip.com/raw","","")
	checkerror(err)
	fmt.Println(" Your IP is: " + ip)
	}

func checkerror(err error){
	if(err!=nil){
	fmt.Printf("err %s detected \n", err)
	os.Exit(1)
	}
	}


func findMyIP(url, marker1 , marker2 string)(myIP string, err error){
	var r *http.Response
	myIP = ""
	r , err = http.Get(url)
	if err!=nil{
	return
	}
	bufreader := bufio.NewReader(r.Body)
	for err == nil {
	var line string
	line, err = bufreader.ReadString('\n')
	if(err != nil){
	return
	}
	if(marker1=="" || marker2==""){
	myIP = line									
	break
	}

	i1 := strings.Index(line,marker1)
				
		if( i1 > -1 ){
	
	i2 := strings.Index(line, marker2)
	myIP = line[i1 + len(marker1) :i2]
	break
	}
	}
	r.Body.Close()
	return
	}
