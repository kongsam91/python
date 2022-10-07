ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      This program gives the weights and points of N point 
c      Gaussian-Legendre quadrature.
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        parameter(n=100)
        double precision x(n),w(n),rin1,rin2,rin3
        open(unit=4,file='gauleg.wx',status='unknown')
        call gauleg(-1d0,1d0,x,w,n)
        rin1=0.d0
        rin2=0.d0
        rin3=0.d0
        do 10 i=1,N
        rin1=rin1+w(i)
        rin2=rin2+w(i)*x(i)**2
10      rin3=rin3+w(i)*dexp(x(i))
        write(6,*) rin1,rin2,rin3
        write(4,99) n
99      !format(1x,t15,'xi',t35,'Wi',t65,'N=',i3)
        do i=1,n
        write(4,*) x(i),w(i)
        end do
        end
cccccccccccccccccccccccccccccccccccccccccccccccccccc
      SUBROUTINE GAULEG(X1,X2,X,W,N)
      IMPLICIT REAL*8 (A-H,O-Z)
      dimension X(N),W(N)
      PARAMETER (EPS=3.D-14)
      M=(N+1)/2
      XM=0.5D0*(X2+X1)
      XL=0.5D0*(X2-X1)
      DO 12 I=1,M
        Z=COS(3.141592654D0*(I-.25D0)/(N+.5D0))
1       CONTINUE
          P1=1.D0
          P2=0.D0
          DO 11 J=1,N
            P3=P2
            P2=P1
            P1=((2.D0*J-1.D0)*Z*P2-(J-1.D0)*P3)/J
11        CONTINUE
          PP=N*(Z*P1-P2)/(Z*Z-1.D0)
          Z1=Z
          Z=Z1-P1/PP
        IF(ABS(Z-Z1).GT.EPS)GO TO 1
        X(I)=XM-XL*Z
        X(N+1-I)=XM+XL*Z
        W(I)=2.D0*XL/((1.D0-Z*Z)*PP*PP)
        W(N+1-I)=W(I)
12    CONTINUE
      RETURN
      END
