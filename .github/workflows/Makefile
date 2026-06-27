IMAGE_NAME=playwright-runner
DOCKERFILE=playwright.dockerfile

.PHONY: test docker-build docker-run ci clean


docker-build:
	docker build -f $(DOCKERFILE) -t $(IMAGE_NAME) .


docker-run:
	docker run --rm \
		-v $(PWD):/app \
		-w /app \
		$(IMAGE_NAME) \
		make test

ci: docker-build docker-run

test:
	pytest -s tests/ --maxfail=1 --disable-warnings -v