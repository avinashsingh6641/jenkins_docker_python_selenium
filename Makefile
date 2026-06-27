IMAGE_NAME=playwright-runner
DOCKERFILE=Playwright.dockerfile

.PHONY: test docker-build docker-run ci clean


docker-build:
	docker build -f $(DOCKERFILE) -t $(IMAGE_NAME) .


docker-run:
	docker run --rm \
		-v $(PWD):/app \
		-w /app \
		$(IMAGE_NAME) \
		make test

ci: 
	make docker-build 
	make docker-run

test:
	pytest -s tests/ --maxfail=1 --disable-warnings -v