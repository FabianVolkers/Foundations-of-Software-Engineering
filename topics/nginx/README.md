# Nginx <!-- omit in TOC -->
## Contents <!-- omit in TOC -->
- [Introduction](#introduction)
- [Use cases](#use-cases)
- [Best practices](#best-practices)
- [Static Files](#static-files)
- [Reverse Proxy](#reverse-proxy)
- [SSL Configuration](#ssl-configuration)
- [Examples](#examples)
  - [Static Files Example](#static-files-example)
  
## Introduction
Nginx (pronounced "engine X", /ˌɛndʒɪnˈɛks/ EN-jin-EKS) (stylized as NGINX or nginx or NginX) is a web server which can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache. The software was created by Igor Sysoev and first publicly released in 2004. A company of the same name was founded in 2011 to provide support and Nginx plus paid software.

Nginx is free and open-source software, released under the terms of the 2-clause BSD license. A large fraction of web servers use NGINX, often as a load balancer.

In March 2019, the Nginx company was acquired by F5 Networks for $670 million.

As of February 2020, Netcraft estimated Nginx served 36.48 percent of all active websites ranked, ranking it first, above Apache at 24.51 percent. while according to W3Techs, Apache is ranked first at 40.1 percent and Nginx 2nd at 31.8 percent.

Source: [Wikipedia](https://en.wikipedia.org/wiki/Nginx)

## Use cases
Nginx is a very powerful piece of software with seemlingly endless configuration options and possibilities. The use cases relevant for the Foundations of SE course are the following
1. Serving static files (HTML, CSS, JavaScript)
2. Reverse proxying requests to services listeningn on specified sockets or ports 

Both of these use cases will be explained further in detail below. It is not uncommon for the two methods to be used in conjunction.

## Best practices
There are a couple of standard ways / best practices of setting up Nginx. The include but are not limited to:
- Save static files in `var/www/<project-name>`
- Create individual configuration files for each project / website in `/etc/nginx/sites-available` and symlink these files into `/etc/nginx/sites-enabled`

## Static Files
Hosting static files is relatively straightforward. All that needs to be done is defining a new server block with a server_name and a root directory of where your static files are located. This should be `var/www/<project-name>`. See [below](#static-files-example) for an example configuration

## Reverse Proxy

## SSL Configuration

## Examples
### Static Files Example
`/etc/nginx/sites-available/example.com`
```
server {
       listen 80;
       listen [::]:80;
       server_name example.com;
       root /var/www/example.com;
       index index.html;
       location / {
               try_files $uri $uri/ =404;
       }
}
```


