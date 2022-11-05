.data
    output: .asciiz "El máximo común divisor es: "
    first: .asciiz "Ingrese el número mayor: "
    second: .asciiz "Ingrese el número menor: "

.text
    main:
        # Ingresamos el primer número
        li $v0, 4
        la $a0, first
        syscall

        li $v0, 5
        syscall
        move $s0, $v0

        # Ingresamos el segundo número
        li $v0, 4
        la $a0, second
        syscall

        li $v0, 5
        syscall
        move $s1, $v0
        
    loop:
        move 	$s2, $s1		# $s2 = $s1
        div     $s0, $s1		# $s0 / $s2
        mfhi    $s3
        move 	$s0, $s1		# $s0 = $s1
        move 	$s1, $s3		# $s1 = $s3
    cond:
        bnez    $s3, loop

        li		$v0, 4		# $v0 = 4
        la		$a0, output		# 
        syscall

        # Output the number
        li      $v0, 1
        move    $a0, $s0
        syscall
        # Exit the program
        li      $v0, 10
        syscall
        