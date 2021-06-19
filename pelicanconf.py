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

CAREER_SUMMARY = 'Deep understanding in developing and maintaining applications running on AWS Cloud Services and Virtualization (Docker, k8s, vagrant, KVM, VirtualBox). Strong experience in Automation as well as CI/CD (Gitlab/Jenkins), monitoring and site-reliability.'

SKILLS = [
	{
		'type': 'LANGUAGES',
		'list': [
			'Bash Shell, Java, Python, PHP, HCL, YAML, JSON'
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

GOOGLE = 'Compute Engine, Cloud Storage, Cloud Build, Cloud Run, Cloud Functions'

AWS = 'EC2, EFS, EKS, ECR, IAM, KMS, Lambda, RDS, Route53, S3, SQS, SNS, SES'

EXPERIENCES = [
	{
		'job_title': 'Cloud Architect',
		'time': 'Nov 2019 – PRESENT',
		'company': 'AtoS Information Technology GmbH',
		'details': '<ul>\
            <li>Conducted research with partners on an assistance system for situation-aware defense of dangers by drones - Google Cloud, AWS, NodeJS, machine learning, IoT</li>\
            <li>Deployed various dockerized apps on private cloud with Docker-Swarm, docker-compose for internal use</li>\
            </ul>'	
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
		'degree': 'Earned Credits towards state examination, first degree\
        <ul><li>Course of study in teaching geography and music</li></ul>',
		'meta': 'Paderborn University',
		'time': 'Oct 1988 - May 1992'
	},
    	{
		'degree': 'Bachelor\'s degree, Telecommunications Engineering',
		'meta': 'HCMC Uniersity of Technology',
		'time': '2006 - 2011'
	}
]

PROJECTS = [
	{
		'title': 'Alarm/Alert System',
		'tagline': {
			'Develop tools with Slack Webhook Integration to monitor product services such as alarm database, alarm renewal certification, service up/down and auto-healing',
			'Monitor replication lag and blocking queries in database',
			'Ensure all Kuberbenets statefulset pods of a service not in same worker node',
			'Alarm and auto-healling core services also important customers sites',
			'Using open source brotandgames /ciao (in Ruby) to health check endpoint URL such as custom domains, API, Zappier, Marketplace, etc.',
			'Monitor scheduled events such as building reports (Business intelligence), alert and auto healing for failed services due to race conditions or system unstable.',
			'Daily scan all ports in AWS Security groups to ensure no open ports to the world except port 80 and 443'
		}
	},
	{
		'title': 'High Availability Core MiddleWare Application',
		'tagline': {
			'Develop Multi-blade service configuration and Multi-blade software management based on OpenSAF source code which provides high availability.',
			'Develop Scale out/in multiple blades feature based on a template node.',
			'Trouble shooting and resolve bugs for correction packages. Plus Schedule delivery project versions to customers. Manage product store (GASK, FTP, PIwin, X-CI, Artifactory).',
			'Analysis and implement requirements/features from customers and responsible for continuous integration and product quality.',
			'Develop and maintain test cases and framework of Function test and System test (JCAT R2/R5 framework) and responsible for CI/CD Jenkins (Eiffel). Support BlueTrain, RDA and LCT, these ones perform regression test for all components in CBA.',
			'Perform all regression tests and light component tests (LCT) for CP versions.',
			'Mentor new members and provide training courses to new comers, share new techniques/ project features.'
		}
	}
]

LANGUAGES = [
	{
		'name': 'German',
		'description': 'Mothertounge'
	},
	{
		'name': 'English',
		'description': 'Professional'
	}
]

INTERESTS = [
	'Yoga',
	'Running'
]
