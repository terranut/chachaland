from django import template
import os

register = template.Library()

def startCode(value, arg):

    return value.replace(arg, "<div class='card-body' style='padding:3px'><pre><code class='language-css'>")

def endCode(value, arg):

    return value.replace(arg, '</code></pre></div>')

def startCita(arg):
	
	static="/static"
	img_quote='<img width="10px" src="{}/svg/badge.svg" alt="badge" style="padding:0px;margin:10px">'.format(static)

	
	return arg.replace('<cita>','<div class="alert alert-warning" role="alert">'+img_quote)

def endCita(arg):

	return arg.replace('</cita>','</div>')




register.filter('startCode', startCode)
register.filter('endCode', endCode)
register.filter('starCita', startCita)
register.filter('endCita', endCita)