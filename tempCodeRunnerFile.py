    while sair != "S":    

                sair = input(f"\n{cores_terminal(5)}Deseja sair? (s/n):{cores_terminal(8)}").capitalize()
                                        
                if sair == "S":
                    print(mensagem_saindo_Ou_voltando("Saindo..."))
                    tempo(3)
                    break
                                            
                elif sair == "N":
                    continue
                                                            
                else:
                    print(f"{cores_terminal(2)}Você só deve informar s ou n")
