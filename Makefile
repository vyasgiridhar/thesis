FILE := main
OUT  := build

.PHONY: pdf
pdf:
	latexmk -f -synctex=1 -interaction=nonstopmode -shell-escape -outdir=$(OUT) -pdf $(FILE)

.PHONY: watch
watch:
	latexmk -interaction=nonstopmode -outdir=$(OUT) -pdf -pvc -halt-on-error $(FILE)

.PHONY: clean
clean:
	rm -rf $(filter-out $(OUT)/$(FILE).pdf, $(wildcard $(OUT)/*))

.PHONY: purge
purge:
	rm -rf $(OUT)
