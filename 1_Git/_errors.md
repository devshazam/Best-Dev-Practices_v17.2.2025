# 
	- key  error: GH013: Repository rule violations found for refs/heads/main
		- desc нарушение правил из-за наличия кода доступа гитхаб в коммите
		- sol удалить из коммита код доступа

	- key changing letter case
		- desc При переименовании при котором меняется только регистр букв - гит не увидит этого!
         	- sol $ git mv old-file-name.ts new-file-name.ts