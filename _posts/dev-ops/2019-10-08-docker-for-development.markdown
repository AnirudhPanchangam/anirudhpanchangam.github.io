---
layout: post
title:  "The All Encompassing Guide to Using Docker + docker-compose for your Development Setup: Part 1"
date:   2019-10-08 18:33:00 +0530
categories: [programming, docker, docker-compose] 
tags: [programming, coding, docker, docker-compose, containers, linux, ubuntu, development]
excerpt_separator: <!--more-->
published: false
---
![Docker Image](/assets/docker.png)  
<!--more-->
[tl;dr](#Let's get started) Link, if you want to skip the half assed introduction and get to the good stuff.

## Introduction ##

I'm making the assumption here that you have a fairly basic understanding of what docker is and  
what it can do for you in terms of speeding up your whole setup of you developmental environment.
If however you would like to get a basic refresher on what docker is, please head over [here](https://docs.docker.com/engine/docker-overview/). If you're lazy like I am and would like a very quick explanation of what it is, here it is.

Docker allows you to run virtual environments like a linux box inside your computer,   
much like a Virtual Machine, but much, much lighter on your system's resources. These running environments are called containers.  
For example, you could run an *Ubuntu-18.04* container on your *Ubuntu-19.04* host. This is pretty cool. 


## Goal ##

Befor we head out on our journey to setup a docker development environemt,  
I believe it is a good idea to define what we want to achieve with this sort of a  
setup.
Let us first define a web based application that we may want to create an environemnt for.  
Let me list my application as having the following dependencies:
    
    - nodejs-10
    - python-3.7.3
    - databases:
        - mongodb
        - postgres
    - cache:
        - redis
    - messaging service:
        - rabbitmq
    - server:
        - nginx

So, to summarize what i've jotted down, our application will have:

1) HTTP service written in **nodejs**.  
2) A python service that listens on queues on rabbitmq.  
3) Databses for all the services.  
4) Redis as a caching service that both the services depends on  
5) Rabbitmq as a message broker that both the python and nodejs service depends on  
6) An nginx server that acts as a reverse proxy for the application. This is however completely optional
   and can be brought in later. This mainly exists if your application in the production strictly depends on a server  for file uploads and various other things like load balancing between multiple workers, etc.  

Now, in my mind, i want it to work like so:  
![Docker Containers](/assets/setup.png)
