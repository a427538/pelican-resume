#!/usr/bin/env python
# -*- coding: utf-8 -*- #

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

THEME = 'theme'

AUTHOR = 'Karl Stich'

SITENAME = 'Resume Karl Stich'

#Profile information
NAME = 'Karl Stich'
TAGLINE = 'Cloud Architect'
PIC = 'profile.png'

#sidebar links
EMAIL = 'stich.karl@gmail.com'
PHONE = '(+49) 1631645275'
LINKEDIN = 'karlstich'
GITHUB = 'a427538'

GITHUB_URL = 'https://github.com/a427538/pelican-resume'

CAREER_SUMMARY = 'Current Cloud Architect at AtoS. An enthusisiastic veteran, 25+ years of advanced Linux experience, hungry to embracing open source software.\
                  Participant at Red Hat Partner Enablement Openshift Curriculum (Consultant Track), advanced knowledge of private, public and hybrid clouds.\
                  Deep understanding in deploying and maintaining applications running on Google Cloud Platform and AWS Cloud Services as well as Container Runtime Environments (Openshift, kubernetes, docker).\
                  Strong experience in Automation (ansible/terraform) as well as CI/CD (Gitlab/Jenkins), monitoring and site-reliability.'

SKILLS = [
	{
		'type': 'LANGUAGES',
		'list': [
			'Bash Shell, Java, Python, , JS, PHP, HCL, YAML, JSON'
		]
	},
	{
		'type': 'FRAMEWORKS',
		'list': [
			'Google Cloud Architecture Framework',
			'Sparx Systems Enterprise Architect',
			'kubernetes, Red Hat Openshift, k3s, etc.'
		]
	},
	{
		'type': 'TOOLS',
		'list': [
			'Postgresql, MariaDB, MySQL, MongoDB, Redis, Cassandra, pgAdmin',
			'VSCode, Gitlab, Github, Jenkins, Ansible, Terraform, Portainer, Traefic',
			'ElasticSearch, Splunk, Kibana, Fluentd/Fluentbit, Grafana, InfluxDB, Prometheus',
			'Bitbucket, Bamboo, Jira, Confluence'
		]
	}
]

GOOGLE = 'Compute Engine, Cloud Storage, Cloud Build, Cloud Run, Cloud Functions, IAM'

AWS = 'EC2, EFS, EKS, ECR, IAM, KMS, Lambda, RDS, Route53, S3, SQS, SNS, SES'

EXPERIENCES = [
	{
		'job_title': 'Cloud Architect',
		'time': 'Nov 2019 – PRESENT',
		'company': 'AtoS Information Technology GmbH',
		'details': '<li>Conducted research with partners on an assistance system for situation-aware defense of dangers by drones - Google Cloud, AWS, NodeJS, machine learning, IoT</li>\
                    <li>Deployed various dockerized apps on private cloud with Docker-Swarm, docker-compose for internal use</li>'	
	},	
	{
		'job_title': 'Senior Consultant',
		'time': 'Aug 2011 – Oct 2019',
		'company': 'AtoS Information Technology GmbH',
		'details': '<ul>\
            <li>Conducted research with partners on an assistance system for situation-aware defense of dangers by drones - Google Cloud, AWS, NodeJS, machine learning, IoT</li>\
            <li>Deployed various dockerized apps on private cloud with Docker-Swarm, docker-compose for internal use</li>\
            </ul>'
	},
		{
		'job_title': 'Senior Consultant',
		'time': 'Jun 2007 – Jul 2011',
		'company': 'Siemens AG (Siemens IT Solution and Services)',
		'details': '<ul>\
            <li>Conducted research with partners on an assistance system for situation-aware defense of dangers by drones - Google Cloud, AWS, NodeJS, machine learning, IoT</li>\
            <li>Deployed various dockerized apps on private cloud with Docker-Swarm, docker-compose for internal use</li>\
            </ul>'
	}
]

EDUCATIONS = [
	{
		'degree': 'Earned credits towards state examination, first degree\
        <ul class="list-unstyled interests-list"><div class="time"><p class="text-light"><li>Course of study in teaching geography and music</li></p></div></ul>',
		'meta': 'Paderborn University',
		'time': 'Oct 1988 - May 1992'
	},
    {
		'degree': 'Earned credits towards graduate engineer\
        <ul class="list-unstyled interests-list"><div class="time"><p class="text-light"><li>Course of study in mechanical engineering</li></p></div></ul>',
		'meta': 'Paderborn University',
		'time': 'Oct 1985 - Oct 1988'
	}
]

PROJECTS = [
	{
		'title': 'Alarm/Alert System',
		'tagline': {
			'Develop tools with Slack Webhook Integration to monitor product services such as alarm database, alarm renewal certification, service up/down and auto-healing'
		}
	},
	{
		'title': 'High Availability Core MiddleWare Application',
		'tagline': {
			'Develop Multi-blade service configuration and Multi-blade software management based on OpenSAF source code which provides high availability.'
		}
	}
]

LANGUAGES = [
	{
		'name': 'German',
		'description': 'Mother tongue'
	},
	{
		'name': 'English',
		'description': 'Professional'
	}
]

INTERESTS = [
	'General Aviation',
	'Music - Soul-Musician (Trumpet) in various Rhythm \'n Soul Bands'
]
