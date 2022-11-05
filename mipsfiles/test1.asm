.data
    message: .asciiz "Hello, World!\n"  # The message to print
.text
    li		$v0, 4		# $v0 = 4
    la		$a0, message		# 
    syscall

    li     $v0, 10
    syscall