library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity LIFO is
	generic (
		DATA_WIDTH : natural := 32;
		ADDR_WIDTH : natural := 10
	);
	port (
        clk_i : in std_ulogic;
        rst_ni : in std_ulogic;
        -- Write Port
        wdata_i : in std_ulogic_vector(DATA_WIDTH-1 downto 0);
        write_i : in std_ulogic;
        -- Read Port
        rdata_o : out std_ulogic_vector(DATA_WIDTH-1 downto 0);
        read_i : in std_ulogic;
        -- Status
        full_o : out std_ulogic;
        empty_o : out std_ulogic
	);
end entity;

architecture rtl of LIFO is

    -- RAM
    type ram_t is array (0 to 2**ADDR_WIDTH-1) of std_ulogic_vector(DATA_WIDTH-1 downto 0);
    signal ram : ram_t;

    signal addr_ff, addr_nxt : std_ulogic_vector(ADDR_WIDTH-1+1 downto 0);

    signal full, empty : std_ulogic;
    signal writing, reading : std_ulogic;

begin
    writing <= write_i and not full;
    reading <= read_i and not empty;

    ram_proc: process(clk_i) is
    begin
        if rising_edge(clk_i) then
            if writing then
                ram(to_integer(unsigned(addr_ff))) <= wdata_i;
            end if;
            if reading then
                rdata_o <= ram(to_integer(unsigned(addr_ff)) - 1);
            end if;
        end if;
    end process;

    seq: process(clk_i) is
    begin
        if rising_edge(clk_i) then
            if not rst_ni then
                addr_ff <= (others => '0');
            else
                addr_ff <= addr_nxt;
            end if;
        end if;
    end process;

    empty <= (nor addr_ff);
    full <= addr_ff(ADDR_WIDTH);

    addr_logic: process (all) is
    begin
        addr_nxt <= addr_ff;

        -- Write but no read
        if writing and not reading then
            addr_nxt <= std_ulogic_vector(unsigned(addr_ff) + 1);
        end if;

        -- Read but no write
        if reading and not writing then
            addr_nxt <= std_ulogic_vector(unsigned(addr_ff) - 1);
        end if;
    end process;

end architecture;