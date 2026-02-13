entity motor_steuerung is
  port (
    clk, areset_n : in  std_ulogic;
    x0, x1        : in  std_ulogic;
    z             : out std_ulogic);
end entity;

architecture RTL of motor_steuerung is
  -- type definitions
  -- s0: Motor aus
  -- s1: Motor an, Knopf noch gedrueckt
  -- s2: Motor an
  -- s3: Motor aus, Knopf noch gedrueckt
  type fsm_t is (s0, s1, s2, s3);

  -- register
  signal state_ff  : fsm_t;
  signal state_nxt : fsm_t;

begin

  seq : process(clk, areset_n)
  begin
    if areset_n = '0' then
      state_ff <= s0;
    elsif rising_edge(clk) then
      state_ff <= state_nxt;
    end if;
  end process;

  zustandsuebergang : process(state_ff)
  begin
    -- default
    state_nxt <= state_ff;

    case state_ff is
      when s0 =>
        if x0 = '1' and x1 = '1' then
          state_nxt <= s1;
        end if;

      when s1 =>
        if x1 = '0' then
          state_nxt <= s2;
        end if;

      when s2 =>
        if x1 = '1' then
          state_nxt <= s3;
        end if;

      when s3 =>
        if x1 = '0' then
          state_nxt <= s0;
        end if;
    end case;
  end process;

  ausgangssignale : process(state_ff)
  begin
    -- default
    z <= '0';
    case state_ff is
      when s0 =>
        if x0 = '1' and x1 = '1' then
          -- Der Motor wird sofort eingeschaltet, nicht erst beim Zustandswechsel
          z <= '1';
        end if;

      when s1 =>
        z <= '1';

      when s2 =>
        -- Der Motor wird (durch die Default-Anweisung) sofort ausgeschaltet, nicht erst beim Zustandswechsel
        if x1 = '0' then
          z <= '1';
        end if;
        
      when s3 =>
        -- wegen Default-Anweisung ist z hier '0'
    end case;
  end process;

end architecture RTL;
