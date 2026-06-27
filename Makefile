IMAGE_NAME=playwright-runner
DOCKERFILE=Playwright.dockerfile

.PHONY: test docker-build docker-run ci debug-docker-workspace clean

test:
	python -m pytest -s tests/ --maxfail=1 --disable-warnings -v

list-workspace:
	pwd
	ls -la

docker-build:
	docker build -f $(DOCKERFILE) -t $(IMAGE_NAME) .

docker-run-test:
	docker run --rm \
		-v $(PWD):/app \
		-w /app \
		$(IMAGE_NAME)\
		sh -c "make list-workspace && make test"
	




