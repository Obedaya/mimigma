# Mimigma

## Changelog

## Introduction

## Installation

### Prerequisites

In order to use Mimigma you need Docker and Docker-compose

---

Clone the repository:
```bash
git clone https://mygit.th-deg.de/mimigma/mimigma.git
```

Go into the directory:
```bash
cd mimigma
```

## Usage

```bash
docker-compose up --build
```

## CI/CD Pipeline

### Triggering Deployments with Git Tags
To trigger a deployment via the CI/CD pipeline, create an annotated tag and push it to the repository. Here is the step-by-step process:

1. Create an annotated tag:
```bash
git tag -a release-x.y.z -m "Release x.y.z"
   ```

2. Push the tag to the repository:
```bash
git push origin release-x.y.z
```

